import { IGeoHub } from './../../interfaces/geo-hub';
import { GeoHubService } from './../../service/geo-hub.service';
import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-geo-hub-list',
  templateUrl: './geo-hub-list.component.html',
  styleUrls: ['./geo-hub-list.component.css'],
})
export class GeoHubListComponent implements OnInit {
  public geoHubs: IGeoHub[] = [
    {
      id: 1,
      crop: 'Potatoes',
      climateRiskScore: 34,
      dateComputed: '2022-11-05T13:25:07.612Z',
      location: 'Helsinki',
    },
    {
      id: 2,
      crop: 'Beans',
      climateRiskScore: 100,
      dateComputed: '2022-11-05T13:25:07.612Z',
      location: 'Oulu',
    },
    {
      id: 3,
      crop: 'Berries',
      climateRiskScore: 73,
      dateComputed: '2022-11-05T13:25:07.612Z',
      location: 'Espoo',
    },
  ];
  displayedColumns: string[] = [
    'location',
    'crop',
    'climateRiskScore',
    'dateComputed',
  ];
  dataSource = new MatTableDataSource(this.geoHubs);

  constructor(private geoHubService: GeoHubService) {}

  ngOnInit(): void {
    // this.geoHubService.getAllGeoHubs();
    // this.geoHubService.geoHub$.subscribe((hub) => {
    //   this.geoHubs = hub;
    // });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }
}
