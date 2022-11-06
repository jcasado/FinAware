package com.example.cassini.dto;

import com.example.cassini.model.GeoHub;
import lombok.Data;

import java.util.Date;

@Data
public class GeoHubDto {

    Integer id;
    String crop;
    Integer climateRiskScore;
    Date dateComputed;
    String location;

    public static GeoHub getGeoHub(GeoHubDto geoHubDto) {
        GeoHub geoHub = new GeoHub();

        geoHub.setId(geoHubDto.getId());
        geoHub.setCrop(geoHubDto.getCrop());
        geoHub.setClimateRiskScore(geoHubDto.getClimateRiskScore());
        geoHub.setDateComputed(geoHubDto.getDateComputed());
        geoHub.setLocation(geoHubDto.getLocation());

        return geoHub;

    }

    public static GeoHubDto getGeoHub(GeoHub geoHub) {
        GeoHubDto geoHubDto = new GeoHubDto();

        geoHubDto.setId(geoHub.getId());
        geoHubDto.setCrop(geoHub.getCrop());
        geoHubDto.setClimateRiskScore(geoHub.getClimateRiskScore());
        geoHubDto.setDateComputed(geoHub.getDateComputed());
        geoHubDto.setLocation(geoHub.getLocation());

        return geoHubDto;

    }
}
