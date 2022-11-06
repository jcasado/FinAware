package com.example.cassini.controller;

import com.example.cassini.dto.GeoHubDto;
import com.example.cassini.service.GeoHubServiceImpl;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("api/finaware")
public class FinawareController {
    @Autowired
    private GeoHubServiceImpl geoHubService;

    @GetMapping("/getGeoHubs")
    @Operation(summary = "Get all GeoHub from system")
    public ResponseEntity<List<GeoHubDto>> getAllGeoHubs() {
        return new ResponseEntity<>(geoHubService.getGeoHubs(), HttpStatus.OK);
    }

    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "GeoHub Found", content = {
                    @Content(mediaType = "application/json", schema = @Schema(implementation = GeoHubDto.class)) }),
            @ApiResponse(responseCode = "400", description = "Invalid id supplied", content = @Content),
            @ApiResponse(responseCode = "404", description = "GeoHub not found", content = @Content) })
    @Operation(summary = "Get GeoHub from system find by location")
    @GetMapping("/getGeoHub/{location}")
    public ResponseEntity<List<GeoHubDto>> getGeoHubByLocation(
            @Parameter(description = "location to search") @RequestParam String location)throws RuntimeException {
        return new ResponseEntity<>(geoHubService.getGeoHubByLocation(location), HttpStatus.OK);
    }

    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "GeoHub Found", content = {
                    @Content(mediaType = "application/json", schema = @Schema(implementation = GeoHubDto.class)) }),
            @ApiResponse(responseCode = "400", description = "Invalid id supplied", content = @Content),
            @ApiResponse(responseCode = "404", description = "getHub not found", content = @Content) })
    @Operation(summary = "Get GeoHub from system find by crop")
    @GetMapping("/getGeoHub/{crop}")
    public ResponseEntity<List<GeoHubDto>> getGeoHubByCrop(
            @Parameter(description = "Asset name") @RequestParam String crop) throws RuntimeException{
        return new ResponseEntity<>(geoHubService.getGeoHubByCrop(crop), HttpStatus.OK);
    }

}
