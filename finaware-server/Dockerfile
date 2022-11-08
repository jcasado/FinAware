FROM maven:3-openjdk-11-slim AS maven
WORKDIR /app
COPY pom.xml .
RUN #mvn -e -B dependency:resolve
COPY src ./src
RUN mvn clean package -DskipTests=true


FROM amazoncorretto:11-alpine-jdk
COPY --from=maven /app/target/*.jar finaware-server.jar

EXPOSE 9000
ENTRYPOINT [ "java", "-jar", "finaware-server.jar"]
