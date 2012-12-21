package main

import (
    "flag"
    "log"
    "net/http"
    "net/url"
)

var target = flag.String("target", "http://www.google.com/", "Where to go.")
var addr = flag.String("listen", ":12345", "Address/port on which to listen.")
var auth = flag.String("auth", "", "Authorization header to add (optional).")

func main() {
    flag.Parse()

    targetUrl, uerr := url.Parse(*target)
    if uerr != nil {
        log.Fatalf("Error parsing target ``%s'': ", target, uerr.String())
    }

    proxy := http.ReverseProxy{Director: func(req *http.Request) {
        req.URL.Scheme = targetUrl.Scheme
        req.URL.Host = targetUrl.Host
        req.Host = targetUrl.Host
        if *auth != "" {
            req.Header.Set("Authorization", *auth)
        }
    }}

    log.Fatal(http.ListenAndServe(*addr, &proxy))
}