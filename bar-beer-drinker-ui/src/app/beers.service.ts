import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface BeerLocation {
  bar: string;
  price: number;
  customers: number;
}

@Injectable({
  providedIn: 'root'
})
export class BeersService {

  constructor(private http: HttpClient) { }

  getItems() {
    return this.http.get<any[]>('/api/items');
  }

  getBarsSelling(item: string) {
    return this.http.get<BeerLocation[]>(`/api/bars-selling/${item}`);
  }

  getBeerManufacturers(item?: string): any {
    if (item) {
      return this.http.get<string>(`/api/beer-manufacturer/${item}`);
    }
    return this.http.get<string[]>('/api/beer-manufacturer');
  }

}
