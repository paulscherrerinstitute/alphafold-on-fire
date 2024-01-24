import { SvelteKitAuth } from '@auth/sveltekit';
import {
	EDU_ID_ISSUER,
	EDU_ID_CLIENT_ID,
	EDU_ID_CLIENT_SECRET
} from '$env/static/private';

export const handle = SvelteKitAuth({
	providers: [
		{
			id: 'eduid',
			name: 'SWITCH edu-ID',
			type: 'oidc',
			issuer: EDU_ID_ISSUER,
			clientId: EDU_ID_CLIENT_ID,
			clientSecret: EDU_ID_CLIENT_SECRET
		}
	]
});
