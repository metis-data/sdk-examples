import { startMetisInstrumentation } from './tracer';
startMetisInstrumentation();

import { NestFactory } from '@nestjs/core';
import { execSync } from 'child_process';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { parse } from 'pg-connection-string';
import { ValidationPipe } from '@nestjs/common';
import { Client } from 'pg';

let client: Client;
async function bootstrap() {
  const connectionString = process.env.PG_CONNECTION_STRING;
  const dbConfig = parse(connectionString);
  client = new Client({ connectionString });
  await client.connect();
  execSync(`psql -U postgres -d ${dbConfig.database} -a -f ./dump.sql`);

  const app = await NestFactory.create(AppModule);

  app.useGlobalPipes(new ValidationPipe({ whitelist: true }));

  const config = new DocumentBuilder()
    .setTitle('Median')
    .setDescription('The Median API description')
    .setVersion('0.1')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  const PORT = process.env.PORT || 3000;

  await app.listen(PORT);
}
bootstrap();
