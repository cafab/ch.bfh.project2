const API_PATH = 'api';

export const AUTH0_CONF = {
    domain: "dev-8bz553ba.eu.auth0.com",
    clientId: "28jTDeN5KjR0NFdke6GQ45x9b2dEDvM1",
    audience: "https://bfh.project2.ch"
};

export const SERVICE_URLS = {
    userUrl: `${API_PATH}/user`
}

export function getFullPath(path) {
    return `http://localhost:5000/${path}`
}