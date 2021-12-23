function getToken() {
    let cookie = document.cookie;
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1);

    return csrfToken;
}