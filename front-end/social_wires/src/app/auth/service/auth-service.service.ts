import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpHeaders, HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  private url = environment.api_url;
  private securityHeaders = new HttpHeaders({
    'Content-Type': 'application/json; charset=utf-8',
  });

  constructor(
    private httpClient: HttpClient
  ) { }

  signUpService( endPoint: string, body:  Record<string, string | number | any> ):any {
    const url = `${this.url}/${endPoint}`;
    return this.httpClient.post(url, body, {headers:this.securityHeaders});
  }

}
