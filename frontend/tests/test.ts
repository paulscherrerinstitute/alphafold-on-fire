import { expect, test } from '@playwright/test';

test('index page has expected h1', async ({ page }) => {
	await page.goto('/');
	await expect(page.getByRole('heading', { name: 'AlphaFold-on-Fire' })).toBeVisible();
});

test('signin page has edu-ID button', async ({ page }) => {
	await page.goto('/auth/signin');
	await expect(
		page.getByRole('button', { name: 'Sign in with SWITCH edu-ID' })
	).toBeVisible();
});
