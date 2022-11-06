package com.example.cassini.repository;

import com.example.cassini.model.GeoHub;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface GeoHubRepository extends JpaRepository<GeoHub, Integer> {

    List<GeoHub> findByLocationContaining(String location);

//    @Query(nativeQuery = true, value = "SELECT * FROM GeoHub g WHERE g.location = ?1 ")
//    List<GeoHub> findByLocation(String location);



}
