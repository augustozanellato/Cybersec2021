'use strict';

function x(g, o) {
    let key = [];
    let ret = "";
    for (let k = 1; k <= 255; k++) key[String.fromCharCode(k)] = k;
    let j = 0;
    for (let z = 0; z < g.length; z++) {
        ret = ret + String.fromCharCode(key[g.substr(z, 1)] ^ key[o.substr(j, 1)]);
        j = j < o.length ? j + 1 : 0
    }
    return ret
};
