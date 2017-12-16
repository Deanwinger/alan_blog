import env from './env';

let conf = {};

if (env === 'debug') {
  conf = {
    server_host: 'http://127.0.0.1:5000/'
  };
} else {
  conf = {
    server_host: 'https://api.lansheng8.com'
  };
}

export default conf;
