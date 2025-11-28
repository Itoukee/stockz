import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class PortfolioService extends Backend {


  constructor(private http: HttpClient) {
    super()
  }

  getPositions(ticker:string) {
    return this.http.get(`${this.url}/dashboard/${ticker}`);
  }

}

