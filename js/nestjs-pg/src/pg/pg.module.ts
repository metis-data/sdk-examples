import { Module } from '@nestjs/common';
import { Pool } from 'pg';
import { PG_CONNECTION } from './pg.consts';

const dbProvider = {
    provide: PG_CONNECTION,
    useValue: new Pool({ connectionString: process.env.DATABASE_URL }),
};

@Module({
    providers: [dbProvider],
    exports: [dbProvider],
})
export class PgModule {}
