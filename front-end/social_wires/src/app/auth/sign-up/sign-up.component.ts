import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';
import { AuthServiceService } from '../service/auth-service.service';
import { ToastrService } from "ngx-toastr";


import { Router } from '@angular/router';


@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {

  registerForm: FormGroup;
  process: string = 'Registrarse';


  constructor(
    private fb: FormBuilder,
    private authService: AuthServiceService,
    private toastr: ToastrService,
    private router: Router,
  ) {
    this.registerForm = this.fb.group({
      nickname: ['', [Validators.required]],
      name: ['', [Validators.required]],
      lastname: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    
    if (this.registerForm.valid) {

      const body = {
        'nickname': this.registerForm.get('nickname')!.value,
        'names': this.registerForm.get('name')!.value,
        'lastname': this.registerForm.get('lastname')!.value,
        'email': this.registerForm.get('email')!.value,
        'password': this.registerForm.get('password')!.value
      }


      this.process = 'Registrando...';
      this.authService.postService(`register_user`, body)
        .subscribe((res: string) => {
          this.router.navigate(['auth/login']);
          this.toastr.success('Usuario registrado con exito', 'Proceso exitoso');
        }, (err: any) => {
          this.toastr.error('ERROR AL INTENTAR AGREGAR USUARIO');
          this.process = 'Registrarse';
        })
    } else {
      Object.keys(this.registerForm.controls).forEach(key => {
        const controlErrors: any = this.registerForm.get(key)!.errors;
        if (controlErrors != null) {
          Object.keys(controlErrors).forEach(keyError => {
            let msg = `${key}: ${keyError} \n`
            this.toastr.error(msg);
          });
        }})
      }
  }

  }
