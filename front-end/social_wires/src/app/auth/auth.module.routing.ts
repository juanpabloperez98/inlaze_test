import { Routes } from '@angular/router';
import { SignUpComponent } from './sign-up/sign-up.component';
import { LoginComponent } from './login/login.component';


export const AuthRoutes: Routes = [
    {
        path: '',
        children:[
            {
                path:'signup',
                component:SignUpComponent
            },
            {
                path:'login',
                component:LoginComponent
            }
        ]
    }
]