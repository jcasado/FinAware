package com.example.cassini.service;

import com.example.cassini.dto.GeoHubDto;
import com.example.cassini.model.GeoHub;
import com.example.cassini.repository.GeoHubRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class GeoHubServiceImpl implements GeoHubServiceI {

    @Autowired
    private GeoHubRepository geoHubRepository;

    @Override
    public List<GeoHubDto> getGeoHubs() {
        List<GeoHub> geoHubList = geoHubRepository.findAll();

        List<GeoHubDto> geoHubDtoList = new ArrayList<>();
        geoHubList.forEach(geoHub -> geoHubDtoList.add(GeoHubDto.getGeoHub(geoHub)));
        return geoHubDtoList;
    }

    @Override
    public List<GeoHubDto> getGeoHubByLocation(String location) throws RuntimeException{
        if (location == null) throw new RuntimeException("Location parameter is empty");

        List<GeoHub> geoHubList = geoHubRepository.findByLocationContaining(location);

        if (geoHubList == null)
            return null;

        List<GeoHubDto> geoHubDtoList = new ArrayList<>();
        geoHubList.forEach(geoHub ->  geoHubDtoList.add(GeoHubDto.getGeoHub(geoHub)));

        return geoHubDtoList;
    }

    @Override
    public List<GeoHubDto> getGeoHubByCrop(String crop) throws RuntimeException{
        List<GeoHubDto> productList = getGeoHubs();

        if (productList == null)
            return null;

        if (crop == null) throw new RuntimeException("Crop parameter is empty");

        List<GeoHubDto> geoHubDtoList = new ArrayList<>();

        if(!productList.isEmpty()){
            productList.forEach(product -> {
                if (product.getLocation().toLowerCase().contains(crop)) {
                    geoHubDtoList.add(product);
                }
            });
        }
        return geoHubDtoList;
    }

}
