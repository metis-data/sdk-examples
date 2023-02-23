import { startMetisInstrumentation } from './tracer';
startMetisInstrumentation();

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { ValidationPipe } from '@nestjs/common';
// import { execSync } from 'child_process';
// import { parse } from 'pg-connection-string';

async function bootstrap() {
  // Seed
  // const connectionString = process.env.DATABASE_URL;
  // const dbConfig = parse(connectionString);
  // execSync(`psql -U postgres -d ${dbConfig.database} -a -f ./dump.sql`);

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
