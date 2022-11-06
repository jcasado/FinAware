package com.example.cassini.service;

import com.example.cassini.dto.GeoHubDto;

import java.util.List;

public interface GeoHubServiceI {
    List<GeoHubDto> getGeoHubs();

    List<GeoHubDto> getGeoHubByLocation(String location) throws RuntimeException;

    List<GeoHubDto> getGeoHubByCrop(String crop)throws RuntimeException;
}
