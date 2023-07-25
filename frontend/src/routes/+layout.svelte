<script lang="ts">
	// SvelteKit Imports
	import { page } from '$app/stores';

	// Components & Utilities
	import { AppShell, AppBar, AppRail, AppRailAnchor, LightSwitch } from '@skeletonlabs/skeleton';

	// Skeleton Stylesheets
	// Your selected Skeleton theme:
	import '@skeletonlabs/skeleton/themes/theme-skeleton.css';
	// This contains the bulk of Skeletons required styles:
	import '@skeletonlabs/skeleton/styles/skeleton.css';
	// Finally, your application's global stylesheet (sometimes labeled 'app.css')
	import '../app.postcss';
</script>

<AppShell slotSidebarLeft="lg:w-auto" slotFooter="bg-black p-4">
	<svelte:fragment slot="header">
		<AppBar>
			<svelte:fragment slot="lead">(psi logo)</svelte:fragment>
			<h1 class="h1">AlphaFold-on-Fire</h1>
			<svelte:fragment slot="trail"><LightSwitch /></svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<AppRail>
			<AppRailAnchor href="/" selected={$page.url.pathname === '/'}>(fa home icon)</AppRailAnchor>
			<AppRailAnchor href="/about" selected={$page.url.pathname === '/about'}>
				(fa about icon)
			</AppRailAnchor>
			<!-- Trail -->
			<svelte:fragment slot="trail">
				<AppRailAnchor
					href="https://github.com/paulscherrerinstitute/alphafold-on-fire"
					target="_blank"
					title="GitHub"
				>
					(fa github icon)
				</AppRailAnchor>
			</svelte:fragment>
		</AppRail>
	</svelte:fragment>
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
	<svelte:fragment slot="pageFooter">Page Footer</svelte:fragment>
	<!-- (footer) -->
</AppShell>
