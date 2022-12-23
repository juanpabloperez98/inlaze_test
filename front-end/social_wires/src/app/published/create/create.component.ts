import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, ValidationErrors } from '@angular/forms';
import { Router } from '@angular/router';
import { PublishedService } from '../service/published.service';
import { ToastrService } from "ngx-toastr";


@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {


  createForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private publishedService: PublishedService,
    private toastr: ToastrService,
  ) {
    this.createForm = this.fb.group({
      title: ['', [Validators.required]],
      message: ['', [Validators.required]],
    });
   }

  ngOnInit(): void {
  }

  onSubmit(){
    if (this.createForm.valid) {
      const body = {
        'title': this.createForm.get('title')!.value,
        'comment': this.createForm.get('message')!.value,
      }
      this.publishedService.postService(`publisheds`, body)
        .subscribe( (res:any) => {
          this.toastr.success('Published post successfully','Success')
          this.createForm = this.fb.group({
            title: ['', [Validators.required]],
            message: ['', [Validators.required]],
          });
        },(err:any) =>{
          this.toastr.error('Published cant post')
        })
    }else{
      Object.keys(this.createForm.controls).forEach(key => {
        const controlErrors: any = this.createForm.get(key)!.errors;
        if (controlErrors != null) {
          Object.keys(controlErrors).forEach(keyError => {
            let msg = `${key}: ${keyError} \n`
            this.toastr.error(msg);
          });
        }})
    }
  }

}
