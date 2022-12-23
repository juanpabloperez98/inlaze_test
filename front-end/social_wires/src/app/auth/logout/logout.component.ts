import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../service/auth-service.service';

import { Router } from '@angular/router';


@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor(
    private authService: AuthServiceService,
    private router: Router,
  ) { 
    this.authService.logOut(`log_out`)
    .subscribe( (res:any) => {
      this.router.navigate(['/auth/login']);
    })
  }
  ngOnInit(): void {}

}
