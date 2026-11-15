// @ts-check
import tseslint from 'typescript-eslint';
import angular from '@angular-eslint/eslint-plugin';
import angularTemplate from '@angular-eslint/eslint-plugin-template';
import angularParser from '@angular-eslint/template-parser';

const FEATURES = [
  'auth',
  'notebook',
  'document',
  'chat',
  'quiz',
  'dashboard',
  'landing',
  'settings',
];

const httpClientBan = {
  name: '@angular/common/http',
  importNames: ['HttpClient'],
  message:
    'HttpClient lives in core/services (ApiService). Pages/components/feature services must use ApiService or a feature service — not HttpClient directly.',
};

const fetchBan = {
  name: 'fetch',
  message: 'Use ApiService / feature services for HTTP. Do not call fetch() in app code.',
};

/** Cross-feature isolation: feature A must not import feature B internals. */
const featureIsolationConfigs = FEATURES.map((feature) => {
  const others = FEATURES.filter((f) => f !== feature);
  return {
    files: [`src/app/features/${feature}/**/*.ts`],
    rules: {
      'no-restricted-imports': [
        'error',
        {
          paths: [httpClientBan],
          patterns: others.map((other) => ({
            group: [`**/features/${other}/**`, `@features/${other}/**`],
            message: `Do not import feature "${other}" from "${feature}". Share via core/ or shared/.`,
          })),
        },
      ],
    },
  };
});

export default tseslint.config(
  {
    ignores: ['dist/**', '.angular/**', 'node_modules/**'],
  },
  {
    files: ['**/*.ts'],
    extends: [...tseslint.configs.recommended],
    plugins: {
      '@angular-eslint': angular,
    },
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
    rules: {
      ...angular.configs.recommended.rules,
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
        },
      ],
      'no-restricted-globals': ['error', fetchBan],
    },
  },
  {
    files: [
      'src/app/features/**/pages/**/*.ts',
      'src/app/features/**/components/**/*.ts',
      'src/app/features/**/services/**/*.ts',
      'src/app/layout/**/*.ts',
      'src/app/shared/**/*.ts',
    ],
    rules: {
      'no-restricted-imports': [
        'error',
        {
          paths: [httpClientBan],
        },
      ],
    },
  },
  {
    files: [
      'src/app/core/services/api.service.ts',
      'src/app/core/interceptors/**/*.ts',
      'src/app/app.config.ts',
    ],
    rules: {
      'no-restricted-imports': 'off',
    },
  },
  ...featureIsolationConfigs,
  {
    files: ['**/*.html'],
    languageOptions: {
      parser: angularParser,
    },
    plugins: {
      '@angular-eslint/template': angularTemplate,
    },
    rules: {
      ...angularTemplate.configs.recommended.rules,
    },
  },
);
