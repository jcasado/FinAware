import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IGeoHub } from '../interfaces/geo-hub';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  }),
};

@Injectable({
  providedIn: 'root',
})
export class GeoHubService {
  public geoHubs: any;
  geoHubURL = environment.apiUrl;
  geoHub: IGeoHub[] = [
    {
      id: 5,
      crop: 'wheat',
      climateRiskScore: 55,
      dateComputed: '2022-11-05T13:25:07.612Z',
      location: 'Vaasa',
    },
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
    {
      id: 4,
      crop: 'Mango',
      climateRiskScore: 24,
      dateComputed: '2022-11-05T13:25:07.612Z',
      location: 'Lapland',
    },
  ];

  geoHub$ = new BehaviorSubject<any>(this.geoHub);

  constructor(private http: HttpClient) {}

  /**
   * Find geoHub from system by title
   * @param location geoHub to be searched
   */
  findgeoHubByLocation(location: string) {
    const URL = this.geoHubURL + `getGeoHub${location}`;

    this.http.get(URL).subscribe({
      next: (response) => {
        this.getAllGeoHubs();
      },
      error(err: HttpErrorResponse) {
        if (err.error instanceof Error) {
          console.log('Client-side error occured.');
        } else {
          console.log('Server-side error occured.');
        }
      },
      complete() {
        console.log('Completed');
      },
    });
  }

  /**
   * Get all geoHubs from the system
   */
  getAllGeoHubs() {
    const url = this.geoHubURL + `getGeoHubs`;
    this.http.get<IGeoHub[]>(url).subscribe({
      next: (response) => {
        this.geoHub$.next(response);
      },
      error(err: HttpErrorResponse) {
        if (err.error instanceof Error) {
          console.log('Client-side error occured.');
        } else {
          console.log('Server-side error occured.');
        }
      },
      complete() {
        console.log('Completed');
      },
    });
  }
}
