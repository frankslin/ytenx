import { Container } from "@cloudflare/containers";

const REDIRECTS = new Map([
  [
    "/byohlyuk/KienxPyan",
    "https://opencc.byvoid.com/characters-easy-to-misuse/",
  ],
]);

export class YtenxContainer extends Container {
  defaultPort = 8000;
  sleepAfter = "30m";

  async fetch(request) {
    await this.startAndWaitForPorts(this.defaultPort);
    return super.fetch(request);
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const redirect = REDIRECTS.get(url.pathname);
    if (redirect) {
      return Response.redirect(redirect, 301);
    }

    const container = env.YTENX_CONTAINER.getByName("ytenx");
    return container.fetch(request);
  },
};
