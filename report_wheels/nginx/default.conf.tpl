

upstream rw_app_server {
        server rw_app:${SERVER_DJANGO_ON};
    }

server {
    listen ${LISTEN_PORT};

    client_max_body_size 100m;
    client_body_buffer_size 100m;
    
    access_log /var/log/nginx/reports_wheels.log;
    error_log /var/log/nginx/reports_wheels_log_error.log;

    client_body_timeout 180;
    client_header_timeout 180;
    keepalive_timeout 180;
    send_timeout 180;



    location /static {
        root /reports_wheels;
    }

    location / {
        proxy_read_timeout 180;
        proxy_connect_timeout 180;
        proxy_send_timeout 180; 
        uwsgi_pass rw_app_server;
        include /etc/nginx/uwsgi_params;

        # Set uWSGI timeout to one day (86400 seconds)
        uwsgi_read_timeout 140;

    }

    location = /favicon.ico { access_log off; log_not_found off; }

   
}
