import { IGeoHub } from './../../interfaces/geo-hub';
import { GeoHubService } from './../../service/geo-hub.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-geo-hub-list',
  templateUrl: './geo-hub-list.component.html',
  styleUrls: ['./geo-hub-list.component.css'],
})
export class GeoHubListComponent implements OnInit {
  public geoHubs: IGeoHub[] = [];
  dataSource = new MatTableDataSource(this.geoHubs);

  @ViewChild(MatPaginator)
  paginator!: MatPaginator;

  displayedColumns: string[] = [
    'location',
    'crop',
    'climateRiskScore',
    'dateComputed',
  ];

  constructor(private geoHubService: GeoHubService) {}

  ngOnInit(): void {
    this.dataSource.paginator = this.paginator;

    this.geoHubService.getAllGeoHubs();
    this.geoHubService.geoHub$.subscribe((hub) => {
      this.geoHubs = hub;
      this.dataSource.data = this.geoHubs;
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}
