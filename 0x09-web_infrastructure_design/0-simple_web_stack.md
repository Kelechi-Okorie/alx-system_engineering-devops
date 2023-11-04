# Explanations of ideas and resources used for task 0  


## What is a Server

A server is a piece of hardware or software that provides functionality for other devices or programs, called clients

## What is the role of a domain name

A domain name is a human readable host name that corresponds to an ip address

## Type of www DNS record in www.foobar.com

CNAME record

## Role of the web server

To server static content over the web using http protocol

## Role of application server

Application server exposes business logic to client applications through various protocols including http

## Role of database

The role of database is to store data in a manner that makes it easy to access and retrieve

## What web server and client uses to communicate

The web server and client uses http to communicate

## SPOF

Single Point Of Failure - This is any part non-redundant part of a system that if redundant would cause the entire system to fail
The single point of failures in this system are the following
- The web server
- The application server
- The database

## Downtown when maintance needed

Since there is no load balancer and no redundant server or replicate database, anytime we want to maintain the site, all traffic to the site will have to be stopped

## Cannot scale if too much incoming traffic

This is because there is only one web server and no load balancer to route and balance requests to the server
