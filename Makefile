local-db-shell:
	PGPASSWORD=${SCOPULI_LOCAL_PG_PASSWORD} \
	psql -U ${SCOPULI_LOCAL_PG_USERNAME} -h ${SCOPULI_LOCAL_PG_HOST} \
	-p ${SCOPULI_LOCAL_PG_PORT} -d ${SCOPULI_LOCAL_PG_DBNAME}

seed-local-db-up: scripts/seed.sh
	PG_HOST=${SCOPULI_LOCAL_PG_HOST} \
	PG_USERNAME=${SCOPULI_LOCAL_PG_USERNAME} \
	PG_PORT=${SCOPULI_LOCAL_PG_PORT} \
	PG_DBNAME=${SCOPULI_LOCAL_PG_DBNAME} \
	PG_PASSWORD=${SCOPULI_LOCAL_PG_PASSWORD} \
	SEED_OPTION=up ENV=local scripts/seed.sh

bootstrap-prod-remote: scripts/bootstrap.sh
	export DAIKON_SSH_KEY=$(< "${DAIKON_SSH_KEY_FILEPATH}")
	ssh -o StrictHostKeyChecking=no ${DAIKON_PROD_HOST} \
		"export DAIKON_DIR=${DAIKON_DIR}; \
		 export DAIKON_SSH_KEY=\"${DAIKON_SSH_KEY}\"; \
		 export DAIKON_ENV=prod; \
		 bash -s" < scripts/bootstrap.sh