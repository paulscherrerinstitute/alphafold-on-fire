import type { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
	webServer: {
		command: 'npm run build && npm run preview',
		port: 4173
	},
	testDir: 'tests',
	testMatch: /(.+\.)?(test|spec)\.[jt]s/,
	// 'github' for GitHub Actions CI to generate annotations, plus a concise 'dot'
	// default 'list' when running locally
	reporter: process.env.CI ? 'github' : 'list',
	// Opt out of parallel tests on CI.
	workers: process.env.CI ? 1 : undefined
};

export default config;
