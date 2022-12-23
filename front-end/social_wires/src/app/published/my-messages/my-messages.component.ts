import { Component, OnInit } from '@angular/core';
import { PublishedService } from '../service/published.service';
import { ToastrService } from "ngx-toastr";
import { PublishedInterface } from '../interfaces/publish.interface';

@Component({
  selector: 'app-my-messages',
  templateUrl: './my-messages.component.html',
  styleUrls: ['./my-messages.component.css']
})
export class MyMessagesComponent implements OnInit {

  publishes: PublishedInterface[];
  loading: true;

  constructor(
    private publishedService: PublishedService,
    private toastr: ToastrService,
  ) { }

  ngOnInit(): void {
    this.publishedService.getService('publisheds')
      .subscribe( (resp:any ) => {
        this.publishes = resp.data;
        console.log(this.publishes);
      },
      (err:any) => {
        console.log(err);
      });
  }

}
