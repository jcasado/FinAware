package com.example.cassini.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity(name = "GeoHub")
public class GeoHub {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    Integer id;

    @Column(name = "crop")
    String crop;

    @Column(name = "crs")
    Integer climateRiskScore;

    @Column(name = "dateComputed")
    Date dateComputed;

    @Column(name = "location")
    String location;
}
