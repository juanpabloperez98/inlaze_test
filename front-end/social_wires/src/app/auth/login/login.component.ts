import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../service/auth-service.service';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';

import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  isSubmited = false;
  loginForm: FormGroup;
  ioauthtoken:string;

  constructor(
    private authService: AuthServiceService,
    private fb: FormBuilder,
    private router: Router,
  ) { 

    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
    })
  }

  ngOnInit(): void {
  }

  onLoginSubmit() {

    if (this.loginForm.valid) {
      this.isSubmited = true;
      const body = {
        'email': this.loginForm.get('email')!.value,
        'password': this.loginForm.get('password')!.value,
      }
      this.authService.postService(`login`, body)
        .subscribe( (res:any) => {
          this.ioauthtoken = res.token;
          this.authService.setToken(this.ioauthtoken);
          this.router.navigate(['/published/create']);
        })
    }
  }


}
