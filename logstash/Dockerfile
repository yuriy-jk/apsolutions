FROM docker.elastic.co/logstash/logstash:7.10.2

RUN /opt/logstash/bin/logstash-plugin install logstash-integration-jdbc
#RUN mkdir /tmp
#RUN curl -o /opt/logstash/vendor/jdbc/postgresql-42.2.18.jar https://jdbc.postgresql.org/download/postgresql-42.2.18.jar
COPY . .
CMD logstash -f logstash-config.conf