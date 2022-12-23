import { NgModule, createComponent } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CreateComponent } from './create/create.component';

// Shared Components
import { HeaderComponent } from '../shared/header/header.component';
import { CardComponent } from '../shared/card/card.component';


import { MyMessagesComponent } from './my-messages/my-messages.component';
import { AllMessagesComponent } from './all-messages/all-messages.component';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    // Shared Component
    CreateComponent,
    CardComponent,
    HeaderComponent,
    MyMessagesComponent,
    AllMessagesComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
  ]
})
export class PublishedModule { }
