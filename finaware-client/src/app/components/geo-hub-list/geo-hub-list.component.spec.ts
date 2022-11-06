import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GeoHubListComponent } from './geo-hub-list.component';

describe('GeoHubListComponent', () => {
  let component: GeoHubListComponent;
  let fixture: ComponentFixture<GeoHubListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GeoHubListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GeoHubListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
