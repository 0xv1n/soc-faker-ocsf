from socfaker import SocFaker

sc = SocFaker()

# Agent
print(sc.agent.ephermeral_id)
print(sc.agent.id)
print(sc.agent.type)
print(sc.agent.name)
print(sc.agent.version)
print(sc.agent)

# Alert
print(sc.alert.summary)
print(sc.alert.signature_name)
print(sc.alert.type)
print(sc.alert.status)
print(sc.alert.action)
print(sc.alert.direction)
print(sc.alert.location)
print(sc.alert)

# Application
print(sc.application.status)
print(sc.application.account_status)
print(sc.application.name)
print(sc.application.logon_timestamp)
print(sc.application)

# Cloud 
print(sc.cloud.id)
print(sc.cloud.zone)
print(sc.cloud.instance_id)
print(sc.cloud.name)
print(sc.cloud.size)
print(sc.cloud.provider)
print(sc.cloud.region)
print(sc.cloud)

# Computer
print(sc.computer.architecture)
print(sc.computer.name)
print(sc.computer.disk)
print(sc.computer.memory)
print(sc.computer.platform)
print(sc.computer.mac_address)
print(sc.computer.os)
print(sc.computer.ipv4)

# Container
print(sc.container.id)
print(sc.container.name)
print(sc.container.tags)
print(sc.container.runtime)
print(sc.container)

# DNS
print(sc.dns.record)
print(sc.dns.header_flags)
print(sc.dns.id)
print(sc.dns.response_code)
print(sc.dns.op_code)
print(sc.dns.answers)
print(sc.dns.question)
print(sc.dns.direction)
print(sc.dns.name)
print(sc.dns)

# Employee
print(sc.employee.name)
print(sc.employee.first_name)
print(sc.employee.last_name)
print(sc.employee.username)
print(sc.employee.email)
print(sc.employee.gender)
print(sc.employee.account_status)
print(sc.employee.ssn)
print(sc.employee.dob)
print(sc.employee.photo)
print(sc.employee.user_id)
print(sc.employee.phone_number)
print(sc.employee.logon_timestamp)
print(sc.employee.language)
print(sc.employee.title)
print(sc.employee.department)
print(sc.employee)

# File
print(sc.file.name)
print(sc.file.extension)
print(sc.file.directory)
print(sc.file.drive_letter)
print(sc.file.gid)
print(sc.file.type)
print(sc.file.mime_type)
print(sc.file.size)
print(sc.file.timestamp)
print(sc.file.accessed_timestamp)
print(sc.file.attributes)
print(sc.file.version)
print(sc.file.build_version)
print(sc.file.checksum)
print(sc.file.install_scope)
print(sc.file.hashes)
print(sc.file.md5)
print(sc.file.sha1)
print(sc.file.sha256)
print(sc.file.full_path)
print(sc.file.signed)
print(sc.file.signature)
print(sc.file.signature_status)
print(sc.file)

# HTTP
print(sc.http.request)
print(sc.http.response)
print(sc.http.status_code)
print(sc.http.method)
print(sc.http.bytes)
print(sc.http)

# Location
print(sc.location.latitude)
print(sc.location.longitude)
print(sc.location.city)
print(sc.location.continent)
print(sc.location.country_code)
print(sc.location.country)
print(sc.location)

# Logs
print(sc.logs.syslog())
print(sc.logs.windows)
print(sc.logs.windows.eventlog())
print(sc.logs.windows.sysmon())
print(sc.logs)

# Network
print(sc.network.ipv4)
print(sc.network.ipv6)
print(sc.network.get_cidr_range('192.168.1.0/24'))
print(sc.network.hostname)
print(sc.network.netbios)
print(sc.network.port)
print(sc.network.protocol)
print(sc.network)

# Operating System
print(sc.operating_system.family)
print(sc.operating_system.name)
print(sc.operating_system.version)
print(sc.operating_system.fullname)
print(sc.operating_system)

# Organization
print(sc.organization.name)
print(sc.organization.domain)
print(sc.organization.division)
print(sc.organization.title)
print(sc.organization)

# PCAP
print(sc.pcap())

# Process 
print(sc.process.args)
print(sc.process.args_count)
print(sc.process.command_line)
print(sc.process.entity_id)
print(sc.process.executable)
print(sc.process.name)
print(sc.process.parent)
print(sc.process.pid)
print(sc.process.start)
print(sc.process.thread_id)
print(sc.process)

# Registry
print(sc.registry.hive)
print(sc.registry.root)
print(sc.registry.key)
print(sc.registry.path)
print(sc.registry.type)
print(sc.registry.value)
print(sc.registry)

# Timestamp
print(sc.timestamp.in_the_past())
print(sc.timestamp.in_the_future())
print(sc.timestamp.current)
print(sc.timestamp.date_string())
print(sc.timestamp)

# Products

## Azure
print(sc.products.azure.vm)
print(sc.products.azure.vm.details)
print(sc.products.azure.vm.metrics)
print(sc.products.azure.vm.metrics.generate())
print(sc.products.azure.vm.metrics.average)
print(sc.products.azure.vm.topology)
print(sc.products.azure)

## Elastic
print(sc.products.elastic.hits(count=1))
print(sc.products.elastic.document)
print(sc.products.elastic.document.fields.agent)
print(sc.products.elastic.document.fields.base)
print(sc.products.elastic.document.fields.client)
print(sc.products.elastic.document.fields.container)
print(sc.products.elastic.document.fields.destination)
print(sc.products.elastic.document.fields.dll)
print(sc.products.elastic.document.fields.dns)
print(sc.products.elastic.document.fields.event)
print(sc.products.elastic.document.fields.file)
print(sc.products.elastic.document.fields.host)
print(sc.products.elastic.document.fields.http)
print(sc.products.elastic.document.fields.network)
print(sc.products.elastic.document.fields.organization)
print(sc.products.elastic.document.fields.package)
print(sc.products.elastic.document.fields.registry)
print(sc.products.elastic.document.fields.server)
print(sc.products.elastic.document.fields.source)
print(sc.products.elastic.document.fields.cloud)
print(sc.products.elastic.document.fields.code_signature)
print(sc.products.elastic.document.fields)

## QualysGuard
print(sc.products.qualysguard.scan(count=1))
print(sc.products.qualysguard)

## ServiceNow
print(sc.products.servicenow.search())
print(sc.products.servicenow)

# User Agent
print(sc.user_agent)

# Vulnerability
print(sc.vulnerability().host.host_id)
print(sc.vulnerability().host.name)
print(sc.vulnerability().host.fqdn)
print(sc.vulnerability().host.mac_address)
print(sc.vulnerability().host.checks_considered)
print(sc.vulnerability().host.percentage)
print(sc.vulnerability().host.total_score)
print(sc.vulnerability().scan.id)
print(sc.vulnerability().scan.scanner_name)
print(sc.vulnerability().scan.scan_uuid)
print(sc.vulnerability().scan.name)
print(sc.vulnerability().scan.type)
print(sc.vulnerability().scan.status)
print(sc.vulnerability().scan.scan_uuid)
print(sc.vulnerability().scan.host_count)
print(sc.vulnerability().scan.ip_list)
print(sc.vulnerability().scan.start_time)
print(sc.vulnerability().scan.end_time)
print(sc.vulnerability().critical)
print(sc.vulnerability().high)
print(sc.vulnerability().medium)
print(sc.vulnerability().low)
print(sc.vulnerability().informational)

# Words
print(sc.words.get())
