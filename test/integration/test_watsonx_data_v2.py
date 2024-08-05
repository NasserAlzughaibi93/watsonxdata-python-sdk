# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for WatsonxDataV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_watsonxdata.watsonx_data_v2 import *

# Config file name
config_file = 'watsonx_data_v2.env'


class TestWatsonxDataV2:
    """
    Integration Test Class for WatsonxDataV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.watsonx_data_service = WatsonxDataV2.new_instance(
            )
            assert cls.watsonx_data_service is not None

            cls.config = read_external_sources(WatsonxDataV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.watsonx_data_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_bucket_registrations(self):
        response = self.watsonx_data_service.list_bucket_registrations(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        bucket_registration_collection = response.get_result()
        assert bucket_registration_collection is not None

    @needscredentials
    def test_create_bucket_registration(self):
        # Construct a dict representation of a BucketDetails model
        bucket_details_model = {
            'access_key': 'b9cbf248ea5c4c96947e64407108559j',
            'bucket_name': 'sample-bucket',
            'endpoint': 'https://s3.<region>.cloud-object-storage.appdomain.cloud/',
            'secret_key': '13b4045cac1a0be54c9fjbe53cb22df5fn397cd2c45b66c87',
        }
        # Construct a dict representation of a BucketCatalog model
        bucket_catalog_model = {
            'catalog_name': 'sampleCatalog',
            'catalog_tags': ['catalog_tag_1', 'catalog_tag_2'],
            'catalog_type': 'iceberg',
        }

        response = self.watsonx_data_service.create_bucket_registration(
            bucket_details=bucket_details_model,
            bucket_type='ibm_cos',
            description='COS bucket for customer data',
            managed_by='ibm',
            associated_catalog=bucket_catalog_model,
            bucket_display_name='sample-bucket-displayname',
            region='us-south',
            tags=['bucket-tag1', 'bucket-tag2'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        bucket_registration = response.get_result()
        assert bucket_registration is not None

    @needscredentials
    def test_get_bucket_registration(self):
        response = self.watsonx_data_service.get_bucket_registration(
            bucket_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        bucket_registration = response.get_result()
        assert bucket_registration is not None

    @needscredentials
    def test_update_bucket_registration(self):
        # Construct a dict representation of a BucketDetails model
        bucket_details_model = {
            'access_key': 'b9cbf248ea5c4c96947e64407108559j',
            'bucket_name': 'sample-bucket',
            'endpoint': 'https://s3.<region>.cloud-object-storage.appdomain.cloud/',
            'secret_key': '13b4045cac1a0be54c9fjbe53cb22df5fn397cd2c45b66c87',
        }
        # Construct a dict representation of a BucketRegistrationPatch model
        bucket_registration_patch_model = {
            'bucket_details': bucket_details_model,
            'bucket_display_name': 'sample-bucket-displayname',
            'description': 'COS bucket for customer data',
            'tags': ['testbucket', 'userbucket'],
        }

        response = self.watsonx_data_service.update_bucket_registration(
            bucket_id='testString',
            body=bucket_registration_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        bucket_registration = response.get_result()
        assert bucket_registration is not None

    @needscredentials
    def test_create_activate_bucket(self):
        response = self.watsonx_data_service.create_activate_bucket(
            bucket_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        create_activate_bucket_created_body = response.get_result()
        assert create_activate_bucket_created_body is not None

    @needscredentials
    def test_list_bucket_objects(self):
        response = self.watsonx_data_service.list_bucket_objects(
            bucket_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        bucket_registration_object_collection = response.get_result()
        assert bucket_registration_object_collection is not None

    @needscredentials
    def test_list_database_registrations(self):
        response = self.watsonx_data_service.list_database_registrations(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        database_registration_collection = response.get_result()
        assert database_registration_collection is not None

    @needscredentials
    def test_create_database_registration(self):
        # Construct a dict representation of a DatabaseCatalog model
        database_catalog_model = {
            'catalog_name': 'sampleCatalog',
            'catalog_tags': ['catalog_tag_1', 'catalog_tag_2'],
            'catalog_type': 'iceberg',
        }
        # Construct a dict representation of a DatabaseDetails model
        database_details_model = {
            'certificate': 'contents of a pem/crt file',
            'certificate_extension': 'pem/crt',
            'database_name': 'new_database',
            'hostname': 'db2@<hostname>.com',
            'hostname_in_certificate': 'samplehostname',
            'hosts': 'abc.com:1234,xyz.com:4321',
            'password': 'samplepassword',
            'port': 4553,
            'sasl': True,
            'ssl': True,
            'tables': 'kafka_table_name',
            'username': 'sampleuser',
            'validate_server_certificate': True,
        }
        # Construct a dict representation of a DatabaseRegistrationPrototypeDatabasePropertiesItems model
        database_registration_prototype_database_properties_items_model = {
            'encrypt': True,
            'key': 'abc',
            'value': 'xyz',
        }

        response = self.watsonx_data_service.create_database_registration(
            database_display_name='new_database',
            database_type='db2',
            associated_catalog=database_catalog_model,
            created_on='1686792721',
            database_details=database_details_model,
            database_properties=[database_registration_prototype_database_properties_items_model],
            description='db2 extenal database description',
            tags=['testdatabase', 'userdatabase'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        database_registration = response.get_result()
        assert database_registration is not None

    @needscredentials
    def test_get_database(self):
        response = self.watsonx_data_service.get_database(
            database_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        database_registration = response.get_result()
        assert database_registration is not None

    @needscredentials
    def test_update_database(self):
        # Construct a dict representation of a DatabaseRegistrationPatchDatabaseDetails model
        database_registration_patch_database_details_model = {
            'password': 'samplepassword',
            'username': 'sampleuser',
        }
        # Construct a dict representation of a DatabaseRegistrationPatch model
        database_registration_patch_model = {
            'database_details': database_registration_patch_database_details_model,
            'database_display_name': 'new_database',
            'description': 'External database description',
            'tags': ['testdatabase', 'userdatabase'],
        }

        response = self.watsonx_data_service.update_database(
            database_id='testString',
            body=database_registration_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        database_registration = response.get_result()
        assert database_registration is not None

    @needscredentials
    def test_list_other_engines(self):
        response = self.watsonx_data_service.list_other_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        other_engine_collection = response.get_result()
        assert other_engine_collection is not None

    @needscredentials
    def test_create_other_engine(self):
        # Construct a dict representation of a OtherEngineDetailsBody model
        other_engine_details_body_model = {
            'connection_string': '1.2.3.4',
            'engine_type': 'netezza',
        }

        response = self.watsonx_data_service.create_other_engine(
            engine_details=other_engine_details_body_model,
            engine_display_name='sampleEngine01',
            description='external engine description',
            origin='external',
            tags=['tag1', 'tag2'],
            type='netezza',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        other_engine = response.get_result()
        assert other_engine is not None

    @needscredentials
    def test_list_db2_engines(self):
        response = self.watsonx_data_service.list_db2_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        db2_engine_collection = response.get_result()
        assert db2_engine_collection is not None

    @needscredentials
    def test_create_db2_engine(self):
        # Construct a dict representation of a Db2EngineDetailsBody model
        db2_engine_details_body_model = {
            'connection_string': '1.2.3.4',
        }

        response = self.watsonx_data_service.create_db2_engine(
            origin='external',
            description='db2 engine description',
            engine_details=db2_engine_details_body_model,
            engine_display_name='sampleEngine',
            tags=['tag1', 'tag2'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        db2_engine = response.get_result()
        assert db2_engine is not None

    @needscredentials
    def test_update_db2_engine(self):
        # Construct a dict representation of a Db2EnginePatch model
        db2_engine_patch_model = {
            'description': 'db2 engine updated description',
            'engine_display_name': 'sampleEngine',
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_db2_engine(
            engine_id='testString',
            body=db2_engine_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        db2_engine = response.get_result()
        assert db2_engine is not None

    @needscredentials
    def test_list_netezza_engines(self):
        response = self.watsonx_data_service.list_netezza_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        netezza_engine_collection = response.get_result()
        assert netezza_engine_collection is not None

    @needscredentials
    def test_create_netezza_engine(self):
        # Construct a dict representation of a NetezzaEngineDetailsBody model
        netezza_engine_details_body_model = {
            'connection_string': '1.2.3.4',
        }

        response = self.watsonx_data_service.create_netezza_engine(
            origin='external',
            description='netezza engine description',
            engine_details=netezza_engine_details_body_model,
            engine_display_name='sampleEngine',
            tags=['tag1', 'tag2'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        netezza_engine = response.get_result()
        assert netezza_engine is not None

    @needscredentials
    def test_update_netezza_engine(self):
        # Construct a dict representation of a NetezzaEnginePatch model
        netezza_engine_patch_model = {
            'description': 'netezza engine updated description',
            'engine_display_name': 'sampleEngine',
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_netezza_engine(
            engine_id='testString',
            body=netezza_engine_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        netezza_engine = response.get_result()
        assert netezza_engine is not None

    @needscredentials
    def test_list_prestissimo_engines(self):
        response = self.watsonx_data_service.list_prestissimo_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        prestissimo_engine_collection = response.get_result()
        assert prestissimo_engine_collection is not None

    @needscredentials
    def test_create_prestissimo_engine(self):
        # Construct a dict representation of a PrestissimoNodeDescriptionBody model
        prestissimo_node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }
        # Construct a dict representation of a PrestissimoEndpoints model
        prestissimo_endpoints_model = {
            'applications_api': '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>',
            'history_server_endpoint': '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server',
            'spark_access_endpoint': '$HOST/analytics-engine/details/spark-<instance_id>',
            'spark_jobs_v4_endpoint': '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications',
            'spark_kernel_endpoint': '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels',
            'view_history_server': 'testString',
            'wxd_application_endpoint': '$HOST/v1/1698311655308796/engines/spark817/applications',
        }
        # Construct a dict representation of a PrestissimoEngineDetails model
        prestissimo_engine_details_model = {
            'api_key': '<api_key>',
            'connection_string': '1.2.3.4',
            'coordinator': prestissimo_node_description_body_model,
            'endpoints': prestissimo_endpoints_model,
            'instance_id': 'instance_id',
            'managed_by': 'fully/self',
            'metastore_host': '1.2.3.4',
            'size_config': 'starter',
            'worker': prestissimo_node_description_body_model,
        }

        response = self.watsonx_data_service.create_prestissimo_engine(
            origin='native',
            associated_catalogs=['hive_data'],
            description='prestissimo engine description',
            engine_details=prestissimo_engine_details_model,
            engine_display_name='sampleEngine',
            region='us-south',
            tags=['tag1', 'tag2'],
            version='1.2.3',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        prestissimo_engine = response.get_result()
        assert prestissimo_engine is not None

    @needscredentials
    def test_get_prestissimo_engine(self):
        response = self.watsonx_data_service.get_prestissimo_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        prestissimo_engine = response.get_result()
        assert prestissimo_engine is not None

    @needscredentials
    def test_update_prestissimo_engine(self):
        # Construct a dict representation of a PrestissimoEnginePropertiesCatalog model
        prestissimo_engine_properties_catalog_model = {
            'catalog_name': ['testString'],
        }
        # Construct a dict representation of a PrestissimoNodeDescriptionBody model
        prestissimo_node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }
        # Construct a dict representation of a EnginePropertiesOaiGenConfiguration model
        engine_properties_oai_gen_configuration_model = {
            'coordinator': prestissimo_node_description_body_model,
            'worker': prestissimo_node_description_body_model,
        }
        # Construct a dict representation of a PrestissimoEnginePropertiesVelox model
        prestissimo_engine_properties_velox_model = {
            'velox_property': ['testString'],
        }
        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }
        # Construct a dict representation of a PrestissimoEnginePropertiesOaiGen1Jvm model
        prestissimo_engine_properties_oai_gen1_jvm_model = {
            'coordinator': node_description_body_model,
        }
        # Construct a dict representation of a PrestissimoEngineEngineProperties model
        prestissimo_engine_engine_properties_model = {
            'catalog': prestissimo_engine_properties_catalog_model,
            'configuration': engine_properties_oai_gen_configuration_model,
            'velox': prestissimo_engine_properties_velox_model,
            'jvm': prestissimo_engine_properties_oai_gen1_jvm_model,
        }
        # Construct a dict representation of a RemoveEnginePropertiesConfiguration model
        remove_engine_properties_configuration_model = {
            'coordinator': ['testString'],
            'worker': ['testString'],
        }
        # Construct a dict representation of a RemoveEngineProperties model
        remove_engine_properties_model = {
            'catalog': prestissimo_engine_properties_catalog_model,
            'configuration': remove_engine_properties_configuration_model,
            'jvm': remove_engine_properties_configuration_model,
            'velox': ['testString'],
        }
        # Construct a dict representation of a PrestissimoEnginePatch model
        prestissimo_engine_patch_model = {
            'description': 'updated description for prestissimo engine',
            'engine_display_name': 'sampleEngine',
            'engine_properties': prestissimo_engine_engine_properties_model,
            'engine_restart': 'force',
            'remove_engine_properties': remove_engine_properties_model,
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_prestissimo_engine(
            engine_id='testString',
            body=prestissimo_engine_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        prestissimo_engine = response.get_result()
        assert prestissimo_engine is not None

    @needscredentials
    def test_list_prestissimo_engine_catalogs(self):
        response = self.watsonx_data_service.list_prestissimo_engine_catalogs(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_add_prestissimo_engine_catalogs(self):
        response = self.watsonx_data_service.add_prestissimo_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_get_prestissimo_engine_catalog(self):
        response = self.watsonx_data_service.get_prestissimo_engine_catalog(
            engine_id='testString',
            catalog_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog = response.get_result()
        assert catalog is not None

    @needscredentials
    def test_pause_prestissimo_engine(self):
        response = self.watsonx_data_service.pause_prestissimo_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_run_prestissimo_explain_statement(self):
        response = self.watsonx_data_service.run_prestissimo_explain_statement(
            engine_id='testString',
            statement='show schemas in catalog_name',
            format='json',
            type='io',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        result_prestissimo_explain_statement = response.get_result()
        assert result_prestissimo_explain_statement is not None

    @needscredentials
    def test_run_prestissimo_explain_analyze_statement(self):
        response = self.watsonx_data_service.run_prestissimo_explain_analyze_statement(
            engine_id='testString',
            statement='show schemas in catalog_name',
            verbose=True,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        result_run_prestissimo_explain_analyze_statement = response.get_result()
        assert result_run_prestissimo_explain_analyze_statement is not None

    @needscredentials
    def test_restart_prestissimo_engine(self):
        response = self.watsonx_data_service.restart_prestissimo_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_resume_prestissimo_engine(self):
        response = self.watsonx_data_service.resume_prestissimo_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_scale_prestissimo_engine(self):
        # Construct a dict representation of a PrestissimoNodeDescriptionBody model
        prestissimo_node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }

        response = self.watsonx_data_service.scale_prestissimo_engine(
            engine_id='testString',
            coordinator=prestissimo_node_description_body_model,
            worker=prestissimo_node_description_body_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 202
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_list_presto_engines(self):
        response = self.watsonx_data_service.list_presto_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        presto_engine_collection = response.get_result()
        assert presto_engine_collection is not None

    @needscredentials
    def test_create_presto_engine(self):
        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }
        # Construct a dict representation of a EngineDetailsBody model
        engine_details_body_model = {
            'api_key': '<api_key>',
            'connection_string': '1.2.3.4',
            'coordinator': node_description_body_model,
            'instance_id': 'instance_id',
            'managed_by': 'fully/self',
            'size_config': 'starter',
            'worker': node_description_body_model,
        }

        response = self.watsonx_data_service.create_presto_engine(
            origin='native',
            associated_catalogs=['iceberg_data', 'hive_data'],
            description='presto engine for running sql queries',
            engine_details=engine_details_body_model,
            engine_display_name='sampleEngine',
            region='us-south',
            tags=['tag1', 'tag2'],
            version='1.2.3',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        presto_engine = response.get_result()
        assert presto_engine is not None

    @needscredentials
    def test_get_presto_engine(self):
        response = self.watsonx_data_service.get_presto_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        presto_engine = response.get_result()
        assert presto_engine is not None

    @needscredentials
    def test_update_presto_engine(self):
        # Construct a dict representation of a PrestoEnginePropertiesCatalog model
        presto_engine_properties_catalog_model = {
            'catalog_name': 'testString',
        }
        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {
            'node_type': 'worker',
            'quantity': 38,
        }
        # Construct a dict representation of a EnginePropertiesOaiGen1Configuration model
        engine_properties_oai_gen1_configuration_model = {
            'coordinator': node_description_body_model,
            'worker': node_description_body_model,
        }
        # Construct a dict representation of a PrestoEnginePropertiesGlobal model
        presto_engine_properties_global_model = {
            'global_property': 'enable-mixed-case-support:true',
        }
        # Construct a dict representation of a EnginePropertiesOaiGen1Jvm model
        engine_properties_oai_gen1_jvm_model = {
            'coordinator': node_description_body_model,
            'worker': node_description_body_model,
        }
        # Construct a dict representation of a PrestoEngineEngineProperties model
        presto_engine_engine_properties_model = {
            'catalog': presto_engine_properties_catalog_model,
            'configuration': engine_properties_oai_gen1_configuration_model,
            'global': presto_engine_properties_global_model,
            'jvm': engine_properties_oai_gen1_jvm_model,
        }
        # Construct a dict representation of a RemoveEnginePropertiesOaiGenConfiguration model
        remove_engine_properties_oai_gen_configuration_model = {
            'coordinator': ['testString'],
            'worker': ['testString'],
        }
        # Construct a dict representation of a RemoveEnginePropertiesOaiGenJvm model
        remove_engine_properties_oai_gen_jvm_model = {
            'coordinator': ['testString'],
            'worker': ['testString'],
        }
        # Construct a dict representation of a PrestoEnginePatchRemoveEngineProperties model
        presto_engine_patch_remove_engine_properties_model = {
            'configuration': remove_engine_properties_oai_gen_configuration_model,
            'jvm': remove_engine_properties_oai_gen_jvm_model,
            'catalog': presto_engine_properties_catalog_model,
        }
        # Construct a dict representation of a PrestoEnginePatch model
        presto_engine_patch_model = {
            'description': 'updated description for presto engine',
            'engine_display_name': 'sampleEngine',
            'engine_properties': presto_engine_engine_properties_model,
            'engine_restart': 'force',
            'remove_engine_properties': presto_engine_patch_remove_engine_properties_model,
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_presto_engine(
            engine_id='testString',
            body=presto_engine_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        presto_engine = response.get_result()
        assert presto_engine is not None

    @needscredentials
    def test_list_presto_engine_catalogs(self):
        response = self.watsonx_data_service.list_presto_engine_catalogs(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_add_presto_engine_catalogs(self):
        response = self.watsonx_data_service.add_presto_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_get_presto_engine_catalog(self):
        response = self.watsonx_data_service.get_presto_engine_catalog(
            engine_id='testString',
            catalog_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog = response.get_result()
        assert catalog is not None

    @needscredentials
    def test_pause_presto_engine(self):
        response = self.watsonx_data_service.pause_presto_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        create_engine_pause_created_body = response.get_result()
        assert create_engine_pause_created_body is not None

    @needscredentials
    def test_run_explain_statement(self):
        response = self.watsonx_data_service.run_explain_statement(
            engine_id='testString',
            statement='show schemas in catalog_name',
            format='json',
            type='io',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        run_explain_statement_ok_body = response.get_result()
        assert run_explain_statement_ok_body is not None

    @needscredentials
    def test_run_explain_analyze_statement(self):
        response = self.watsonx_data_service.run_explain_analyze_statement(
            engine_id='testString',
            statement='show schemas in catalog_name',
            verbose=True,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        run_explain_analyze_statement_ok_body = response.get_result()
        assert run_explain_analyze_statement_ok_body is not None

    @needscredentials
    def test_restart_presto_engine(self):
        response = self.watsonx_data_service.restart_presto_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        create_engine_restart_created_body = response.get_result()
        assert create_engine_restart_created_body is not None

    @needscredentials
    def test_resume_presto_engine(self):
        response = self.watsonx_data_service.resume_presto_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        create_engine_resume_created_body = response.get_result()
        assert create_engine_resume_created_body is not None

    @needscredentials
    def test_scale_presto_engine(self):
        # Construct a dict representation of a NodeDescription model
        node_description_model = {
            'node_type': 'worker',
            'quantity': 38,
        }

        response = self.watsonx_data_service.scale_presto_engine(
            engine_id='testString',
            coordinator=node_description_model,
            worker=node_description_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 202
        create_engine_scale_created_body = response.get_result()
        assert create_engine_scale_created_body is not None

    @needscredentials
    def test_list_spark_engines(self):
        response = self.watsonx_data_service.list_spark_engines(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        spark_engine_collection = response.get_result()
        assert spark_engine_collection is not None

    @needscredentials
    def test_create_spark_engine(self):
        # Construct a dict representation of a SparkDefaultConfig model
        spark_default_config_model = {
            'config1': 'testString',
            'config2': 'testString',
        }
        # Construct a dict representation of a SparkScaleConfig model
        spark_scale_config_model = {
            'auto_scale_enabled': True,
            'current_number_of_nodes': 2,
            'maximum_number_of_nodes': 5,
            'minimum_number_of_nodes': 1,
            'node_type': 'small',
            'number_of_nodes': 5,
        }
        # Construct a dict representation of a SparkEngineDetailsPrototype model
        spark_engine_details_prototype_model = {
            'api_key': 'apikey',
            'connection_string': '1.2.3.4',
            'default_config': spark_default_config_model,
            'default_version': '3.3',
            'engine_home_bucket_display_name': 'test-spark-bucket',
            'engine_home_bucket_name': '4fec0f8b-888a-4c16-8f38-250c8499e6ce-customer',
            'engine_home_path': 'spark/spark1234',
            'engine_home_volume_id': '1704979825978585',
            'engine_home_volume_name': 'my-volume',
            'engine_home_volume_storage_class': 'nfs-client',
            'engine_home_volume_storage_size': '5Gi',
            'instance_id': 'spark-id',
            'managed_by': 'fully/self',
            'scale_config': spark_scale_config_model,
        }

        response = self.watsonx_data_service.create_spark_engine(
            origin='native',
            associated_catalogs=['iceberg_data'],
            description='testString',
            engine_details=spark_engine_details_prototype_model,
            engine_display_name='test-native',
            status='testString',
            tags=['testString'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 202
        spark_engine = response.get_result()
        assert spark_engine is not None

    @needscredentials
    def test_get_spark_engine(self):
        response = self.watsonx_data_service.get_spark_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        spark_engine = response.get_result()
        assert spark_engine is not None

    @needscredentials
    def test_update_spark_engine(self):
        # Construct a dict representation of a UpdateSparkEngineBodyEngineDetails model
        update_spark_engine_body_engine_details_model = {
            'default_config': {'config1': 'value1', 'config2': 'value2'},
            'default_version': '3.4',
        }
        # Construct a dict representation of a UpdateSparkEngineBody model
        update_spark_engine_body_model = {
            'description': 'Updated Description',
            'engine_details': update_spark_engine_body_engine_details_model,
            'engine_display_name': 'Updated Display Name',
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_spark_engine(
            engine_id='testString',
            body=update_spark_engine_body_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        spark_engine = response.get_result()
        assert spark_engine is not None

    @needscredentials
    def test_list_spark_engine_applications(self):
        response = self.watsonx_data_service.list_spark_engine_applications(
            engine_id='testString',
            auth_instance_id='testString',
            state=['testString'],
        )

        assert response.get_status_code() == 200
        spark_engine_application_status_collection = response.get_result()
        assert spark_engine_application_status_collection is not None

    @needscredentials
    def test_create_spark_engine_application(self):
        # Construct a dict representation of a SparkApplicationConfig model
        spark_application_config_model = {
            'spark_sample_config_properpty': 'testString',
        }
        # Construct a dict representation of a SparkApplicationEnv model
        spark_application_env_model = {
            'sample_env_key': 'testString',
        }
        # Construct a dict representation of a SparkApplicationDetails model
        spark_application_details_model = {
            'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
            'arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt'],
            'class': 'org.apache.spark.examples.SparkPi',
            'conf': spark_application_config_model,
            'env': spark_application_env_model,
            'files': 's3://mybucket/myfile.txt',
            'jars': 'testString',
            'name': 'SparkApplicaton1',
            'packages': 'org.apache.spark:example_1.2.3',
            'repositories': 'https://repo1.maven.org/maven2/',
            'spark_version': '3.3',
        }
        # Construct a dict representation of a SparkVolumeDetails model
        spark_volume_details_model = {
            'mount_path': '/mount/path',
            'name': 'my-volume',
            'read_only': True,
            'source_sub_path': '/source/path',
        }

        response = self.watsonx_data_service.create_spark_engine_application(
            engine_id='testString',
            application_details=spark_application_details_model,
            job_endpoint='testString',
            service_instance_id='testString',
            type='iae',
            volumes=[spark_volume_details_model],
            auth_instance_id='testString',
            state=['testString'],
        )

        assert response.get_status_code() == 201
        spark_engine_application_status = response.get_result()
        assert spark_engine_application_status is not None

    @needscredentials
    def test_get_spark_engine_application_status(self):
        response = self.watsonx_data_service.get_spark_engine_application_status(
            engine_id='testString',
            application_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        spark_engine_application_status = response.get_result()
        assert spark_engine_application_status is not None

    @needscredentials
    def test_list_spark_engine_catalogs(self):
        response = self.watsonx_data_service.list_spark_engine_catalogs(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_add_spark_engine_catalogs(self):
        response = self.watsonx_data_service.add_spark_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_get_spark_engine_catalog(self):
        response = self.watsonx_data_service.get_spark_engine_catalog(
            engine_id='testString',
            catalog_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog = response.get_result()
        assert catalog is not None

    @needscredentials
    def test_get_spark_engine_history_server(self):
        response = self.watsonx_data_service.get_spark_engine_history_server(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        spark_history_server = response.get_result()
        assert spark_history_server is not None

    @needscredentials
    def test_start_spark_engine_history_server(self):
        response = self.watsonx_data_service.start_spark_engine_history_server(
            engine_id='testString',
            cores='1',
            memory='4G',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        spark_history_server = response.get_result()
        assert spark_history_server is not None

    @needscredentials
    def test_create_spark_engine_pause(self):
        response = self.watsonx_data_service.create_spark_engine_pause(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_create_spark_engine_resume(self):
        response = self.watsonx_data_service.create_spark_engine_resume(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_create_spark_engine_scale(self):
        response = self.watsonx_data_service.create_spark_engine_scale(
            engine_id='testString',
            number_of_nodes=2,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        success_response = response.get_result()
        assert success_response is not None

    @needscredentials
    def test_list_spark_versions(self):
        response = self.watsonx_data_service.list_spark_versions(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        list_spark_versions_ok_body = response.get_result()
        assert list_spark_versions_ok_body is not None

    @needscredentials
    def test_list_catalogs(self):
        response = self.watsonx_data_service.list_catalogs(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog_collection = response.get_result()
        assert catalog_collection is not None

    @needscredentials
    def test_get_catalog(self):
        response = self.watsonx_data_service.get_catalog(
            catalog_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        catalog = response.get_result()
        assert catalog is not None

    @needscredentials
    def test_list_schemas(self):
        response = self.watsonx_data_service.list_schemas(
            engine_id='testString',
            catalog_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        list_schemas_ok_body = response.get_result()
        assert list_schemas_ok_body is not None

    @needscredentials
    def test_create_schema(self):
        response = self.watsonx_data_service.create_schema(
            engine_id='testString',
            catalog_id='testString',
            custom_path='sample-path',
            schema_name='SampleSchema1',
            bucket_name='sample-bucket',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        create_schema_created_body = response.get_result()
        assert create_schema_created_body is not None

    @needscredentials
    def test_list_tables(self):
        response = self.watsonx_data_service.list_tables(
            catalog_id='testString',
            schema_id='testString',
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        table_collection = response.get_result()
        assert table_collection is not None

    @needscredentials
    def test_get_table(self):
        response = self.watsonx_data_service.get_table(
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        table = response.get_result()
        assert table is not None

    @needscredentials
    def test_rename_table(self):
        # Construct a dict representation of a TablePatch model
        table_patch_model = {
            'table_name': 'updated_table_name',
        }

        response = self.watsonx_data_service.rename_table(
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            engine_id='testString',
            body=table_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        table = response.get_result()
        assert table is not None

    @needscredentials
    def test_list_columns(self):
        response = self.watsonx_data_service.list_columns(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        column_collection = response.get_result()
        assert column_collection is not None

    @needscredentials
    def test_create_columns(self):
        # Construct a dict representation of a Column model
        column_model = {
            'column_name': 'expenses',
            'comment': 'expenses column',
            'extra': 'varchar',
            'length': '30',
            'scale': '2',
            'type': 'varchar',
        }

        response = self.watsonx_data_service.create_columns(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            columns=[column_model],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        column_collection = response.get_result()
        assert column_collection is not None

    @needscredentials
    def test_update_column(self):
        # Construct a dict representation of a ColumnPatch model
        column_patch_model = {
            'column_name': 'expenses',
        }

        response = self.watsonx_data_service.update_column(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            column_id='testString',
            body=column_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        column = response.get_result()
        assert column is not None

    @needscredentials
    def test_list_table_snapshots(self):
        response = self.watsonx_data_service.list_table_snapshots(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        table_snapshot_collection = response.get_result()
        assert table_snapshot_collection is not None

    @needscredentials
    def test_rollback_table(self):
        response = self.watsonx_data_service.rollback_table(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            snapshot_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        replace_snapshot_created_body = response.get_result()
        assert replace_snapshot_created_body is not None

    @needscredentials
    def test_update_sync_catalog(self):
        # Construct a dict representation of a SyncCatalogs model
        sync_catalogs_model = {
            'auto_add_new_tables': True,
            'sync_iceberg_md': True,
        }

        response = self.watsonx_data_service.update_sync_catalog(
            catalog_id='testString',
            body=sync_catalogs_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        update_sync_catalog_ok_body = response.get_result()
        assert update_sync_catalog_ok_body is not None

    @needscredentials
    def test_list_milvus_services(self):
        response = self.watsonx_data_service.list_milvus_services(
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        milvus_service_collection = response.get_result()
        assert milvus_service_collection is not None

    @needscredentials
    def test_create_milvus_service(self):
        response = self.watsonx_data_service.create_milvus_service(
            origin='native',
            description='milvus service for running sql queries',
            service_display_name='sampleService',
            tags=['tag1', 'tag2'],
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 201
        milvus_service = response.get_result()
        assert milvus_service is not None

    @needscredentials
    def test_get_milvus_service(self):
        response = self.watsonx_data_service.get_milvus_service(
            service_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        milvus_service = response.get_result()
        assert milvus_service is not None

    @needscredentials
    def test_update_milvus_service(self):
        # Construct a dict representation of a MilvusServicePatch model
        milvus_service_patch_model = {
            'description': 'updated description for milvus service',
            'service_display_name': 'sampleService',
            'tags': ['tag1', 'tag2'],
        }

        response = self.watsonx_data_service.update_milvus_service(
            service_id='testString',
            body=milvus_service_patch_model,
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 200
        milvus_service = response.get_result()
        assert milvus_service is not None

    @needscredentials
    def test_list_ingestion_jobs(self):
        response = self.watsonx_data_service.list_ingestion_jobs(
            auth_instance_id='testString',
            start='1',
            jobs_per_page=1,
        )

        assert response.get_status_code() == 200
        ingestion_job_collection = response.get_result()
        assert ingestion_job_collection is not None

    @needscredentials
    def test_list_ingestion_jobs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = IngestionJobsPager(
            client=self.watsonx_data_service,
            auth_instance_id='testString',
            jobs_per_page=1,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = IngestionJobsPager(
            client=self.watsonx_data_service,
            auth_instance_id='testString',
            jobs_per_page=1,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_ingestion_jobs() returned a total of {len(all_results)} items(s) using IngestionJobsPager.')

    @needscredentials
    def test_deregister_bucket(self):
        response = self.watsonx_data_service.deregister_bucket(
            bucket_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_deactivate_bucket(self):
        response = self.watsonx_data_service.delete_deactivate_bucket(
            bucket_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_database_catalog(self):
        response = self.watsonx_data_service.delete_database_catalog(
            database_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_other_engine(self):
        response = self.watsonx_data_service.delete_other_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_db2_engine(self):
        response = self.watsonx_data_service.delete_db2_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_netezza_engine(self):
        response = self.watsonx_data_service.delete_netezza_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_prestissimo_engine(self):
        response = self.watsonx_data_service.delete_prestissimo_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_prestissimo_engine_catalogs(self):
        response = self.watsonx_data_service.delete_prestissimo_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_engine(self):
        response = self.watsonx_data_service.delete_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_presto_engine_catalogs(self):
        response = self.watsonx_data_service.delete_presto_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_spark_engine(self):
        response = self.watsonx_data_service.delete_spark_engine(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_spark_engine_applications(self):
        response = self.watsonx_data_service.delete_spark_engine_applications(
            engine_id='testString',
            application_id='testString',
            auth_instance_id='testString',
            state=['testString'],
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_spark_engine_catalogs(self):
        response = self.watsonx_data_service.delete_spark_engine_catalogs(
            engine_id='testString',
            catalog_names='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_spark_engine_history_server(self):
        response = self.watsonx_data_service.delete_spark_engine_history_server(
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_schema(self):
        response = self.watsonx_data_service.delete_schema(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_table(self):
        response = self.watsonx_data_service.delete_table(
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            engine_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_column(self):
        response = self.watsonx_data_service.delete_column(
            engine_id='testString',
            catalog_id='testString',
            schema_id='testString',
            table_id='testString',
            column_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_milvus_service(self):
        response = self.watsonx_data_service.delete_milvus_service(
            service_id='testString',
            auth_instance_id='testString',
        )

        assert response.get_status_code() == 204
