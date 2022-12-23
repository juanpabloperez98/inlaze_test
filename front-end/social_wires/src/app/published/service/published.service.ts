import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient, HttpParams } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { AuthServiceService } from 'src/app/auth/service/auth-service.service';



@Injectable({
  providedIn: 'root'
})
export class PublishedService {

  private url = environment.api_url;
  private securityHeaders = new HttpHeaders({
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': `token ${ this.authService.getToken() }`
  });


  constructor(
    private httpClient: HttpClient,
    private authService: AuthServiceService,
  ) { }

  postService( endPoint: string, body:  Record<string, string | number | any> ):any {
    const url = `${this.url}/${endPoint}`;
    return this.httpClient.post(url, body, {headers:this.securityHeaders});
  }

  getService( endPoint: string ):any {
    const url = `${this.url}/${endPoint}`;
    return this.httpClient.get(url, {headers:this.securityHeaders});
  }

  /* getParamsService( endPoint: string, body:  Record<string, string | number | any> ):any {
    const url = `${this.url}/${endPoint}`;
    return this.httpClient.post(url, body, {headers:this.securityHeaders});
  } */
}
