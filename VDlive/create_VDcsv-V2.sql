USE [5G_2022]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[VDcsv](
	[UpdateTime] [datetime] NULL,
	[vdid] [varchar](50) NULL,
	[linkid] [varchar](50) NULL,
	[laneid] [varchar](10) NULL,
	[lanetype] [char](1) NULL,
	[speed] [float] NULL,
	[occupancy] [float] NULL,
	[vehicletype] [char](1) NULL,
	[volume] [float] NULL,
	[speed2] [float] NULL,
	[status] [char](1) NULL,
	[datacollecttime] [datetime] NULL
) ON [PRIMARY]
GO


