import { setInstrumentedPrismaClient } from "@metis-data/prisma-interceptor";
import { INestApplication, Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
  constructor() {
    super({
      log: [{
        emit: "event",
        level: "query",
      }]
});
  }
  
  async enableShutdownHooks(app: INestApplication) {
    this.$on('beforeExit', async () => {
      await app.close();
    });
  }

  async onModuleInit() {
    setInstrumentedPrismaClient(this)
  }
}
