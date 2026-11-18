// Small glob matcher for POSIX relative paths: `*`, `?`, `**` (any number of
// directories, including none) and `{a,b}` alternatives with literal parts.

const cache = new Map();

function escapeLiteral(text) {
  return text.replace(/[.+^$()|[\]\\{}*?]/g, '\\$&');
}

export function globToRegExp(pattern) {
  if (cache.has(pattern)) return cache.get(pattern);
  let source = '';
  for (let index = 0; index < pattern.length; index += 1) {
    const char = pattern[index];
    if (char === '*') {
      if (pattern[index + 1] === '*') {
        const atSegmentStart = index === 0 || pattern[index - 1] === '/';
        const next = pattern[index + 2];
        if (atSegmentStart && next === '/') { source += '(?:.*/)?'; index += 2; continue; }
        source += '.*';
        index += 1;
        continue;
      }
      source += '[^/]*';
    } else if (char === '?') {
      source += '[^/]';
    } else if (char === '{') {
      const end = pattern.indexOf('}', index);
      if (end === -1) throw new Error(`glob thiếu "}": ${pattern}`);
      const choices = pattern.slice(index + 1, end).split(',').map(escapeLiteral);
      source += `(?:${choices.join('|')})`;
      index = end;
    } else {
      source += escapeLiteral(char);
    }
  }
  const regExp = new RegExp(`^${source}$`);
  cache.set(pattern, regExp);
  return regExp;
}

export function matchesGlob(relativePath, pattern) {
  return globToRegExp(pattern).test(relativePath);
}

export function matchesAny(relativePath, patterns = []) {
  return patterns.some((pattern) => matchesGlob(relativePath, pattern));
}
