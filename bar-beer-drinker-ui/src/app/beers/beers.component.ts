import { Component, OnInit } from '@angular/core';
import { BeersService } from '../beers.service';
import { SelectItem } from 'primeng/components/common/selectitem';

@Component({
  selector: 'app-beers',
  templateUrl: './beers.component.html',
  styleUrls: ['./beers.component.css']
})
export class BeersComponent implements OnInit {

  items: any[];
  manufacturerOptions: SelectItem[];

  originalItemsList: any[];

  constructor(private beerService: BeersService) {
    this.beerService.getItems().subscribe(
      data => {
        this.items = data;
        this.originalItemsList = data;
      }
    );
    this.beerService.getBeerManufacturers().subscribe(
      data => {
        this.manufacturerOptions = data.map(manf => {
          return {
            label: manf,
            value: manf,
          };
        });
      }
    );
  }

  ngOnInit() {
  }

  filterBeers(manufacturer: string) {
    this.items = this.originalItemsList;
    if (manufacturer) {
      this.items = this.originalItemsList.filter(item => item.manufacturer === manufacturer);
    }
  }

}
