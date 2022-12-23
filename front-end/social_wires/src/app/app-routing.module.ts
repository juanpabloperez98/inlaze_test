import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { SignUpComponent } from './auth/sign-up/sign-up.component';
import { CreateComponent } from './published/create/create.component';
import { MyMessagesComponent } from './published/my-messages/my-messages.component';
import { AllMessagesComponent } from './published/all-messages/all-messages.component';
import { AuthGuard } from './auth/guards/auth.guard';
import { LogoutComponent } from './auth/logout/logout.component';



export const Approutes: Routes = [
    {
        path:'auth/login',
        component: LoginComponent,
        pathMatch:'full'
    },
    {
        path:'auth/signup',
        component: SignUpComponent,
        pathMatch:'full'
    },
    {
        path:'auth/logout',
        component: LogoutComponent,
        pathMatch:'full'
    },
    {
        path:'published/create',
        component:CreateComponent,
        canActivate:[AuthGuard],
        pathMatch:'full',
    },
    {
        path:'published/my_messages',
        component:MyMessagesComponent,
        canActivate:[AuthGuard],
        pathMatch:'full',
    },
    {
        path:'published/messages',
        component:AllMessagesComponent,
        canActivate:[AuthGuard],
        pathMatch:'full',
    },
    {
        path: '**',
        redirectTo: '/auth/login'
    }
]