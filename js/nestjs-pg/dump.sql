CREATE TABLE IF NOT EXISTS "article" (
   "id" SERIAL NOT NULL,
   "title" TEXT NOT NULL,
   "description" TEXT,
   "body" TEXT NOT NULL,
   "published" BOOLEAN NOT NULL DEFAULT false,
   "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

   CONSTRAINT "article_pkey" PRIMARY KEY ("id")
);

CREATE UNIQUE INDEX "article_title_key" ON "article"("title");

INSERT INTO "article" ("title", "body", "description", "published")
  VALUES
    (
     'Pg Adds Support for MongoDB',
     'Support for MongoDB has been one of the most requested features since the initial release of...',
     'We are excited to share that todays pg driver release adds stable support for MongoDB!',
     false
    ),
    (
     'Whats new in Pg? (Q1/22)',
     'Our engineers have been working hard, issuing new releases with many improvements...',
     'Learn about everything in the Pg ecosystem and community from January to March 2022.',
     true
    )
  ON CONFLICT DO NOTHING;