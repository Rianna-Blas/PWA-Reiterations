if("serviceworler" in navigator) {
    window.addEventListener("load", function () {
        this.navigator.serviceWorker
        .register("static/js/serviceworker.js")
        .then((res) => console.log("service worker registered"))
        .catch((err) => console.log("service worker not registered"))
    });
}