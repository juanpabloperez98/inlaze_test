import { Routes } from '@angular/router';
import { SignUpComponent } from './sign-up/sign-up.component';

export const AuthRoutes: Routes = [
    {
        path: '',
        children:[
            {
                path:'signup',
                component:SignUpComponent
            }
        ]
    }
]