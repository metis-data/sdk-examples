// src/main.ts

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { ValidationPipe } from '@nestjs/common';
import { PrismaNestInterceptor } from '@metis-data/prisma-nest-interceptor';

const { METIS_SERVICE_NAME: serviceName, METIS_SERVICE_VERSION: serviceVersion, METIS_API_KEY: apiKey } = process.env;

const interceptor = PrismaNestInterceptor.create({
  serviceName,
  serviceVersion,
  apiKey
});

interceptor.instrument({ excludedUrls: [/favicon.ico/] });

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.useGlobalPipes(new ValidationPipe({ whitelist: true }));

  const config = new DocumentBuilder()
    .setTitle('Median')
    .setDescription('The Median API description')
    .setVersion('0.1')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.listen(3000);
}
bootstrap();
