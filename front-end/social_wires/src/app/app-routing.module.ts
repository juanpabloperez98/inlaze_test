import { Routes } from '@angular/router';


export const Approutes: Routes = [
    {
        path: 'auth',
        children:[
            {
                path: '',
                loadChildren: () => import('./auth/auth.module').then(x => x.AuthModule)
            }
        ]
    },
    {
        path: '**',
        redirectTo: '/auth/login'
    }
]