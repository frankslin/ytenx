import { Container } from "@cloudflare/containers";

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
    const container = env.YTENX_CONTAINER.getByName("ytenx");
    return container.fetch(request);
  },
};
