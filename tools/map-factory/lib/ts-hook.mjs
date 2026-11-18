import { registerHooks } from 'node:module';
import path from 'node:path';

// Let Node strip types; only fill in extensionless relative TypeScript imports.
registerHooks({
  resolve(specifier, context, nextResolve) {
    try {
      return nextResolve(specifier, context);
    } catch (error) {
      const relative = specifier.startsWith('./') || specifier.startsWith('../');
      if (relative && path.extname(specifier) === '' && context.parentURL?.endsWith('.ts')) {
        return nextResolve(`${specifier}.ts`, context);
      }
      throw error;
    }
  },
});
